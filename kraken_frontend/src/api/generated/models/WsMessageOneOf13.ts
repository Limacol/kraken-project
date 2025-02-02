/* tslint:disable */
/* eslint-disable */
/**
 * kraken
 * The core component of kraken-project
 *
 * The version of the OpenAPI document: 0.1.0
 * Contact: git@omikron.dev
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
import type { SimpleHost } from './SimpleHost';
import {
    SimpleHostFromJSON,
    SimpleHostFromJSONTyped,
    SimpleHostToJSON,
} from './SimpleHost';

/**
 * A new host was found
 * @export
 * @interface WsMessageOneOf13
 */
export interface WsMessageOneOf13 {
    /**
     * The workspace this host is related to
     * @type {string}
     * @memberof WsMessageOneOf13
     */
    workspace: string;
    /**
     * 
     * @type {SimpleHost}
     * @memberof WsMessageOneOf13
     */
    host: SimpleHost;
    /**
     * 
     * @type {string}
     * @memberof WsMessageOneOf13
     */
    type: WsMessageOneOf13TypeEnum;
}


/**
 * @export
 */
export const WsMessageOneOf13TypeEnum = {
    NewHost: 'NewHost'
} as const;
export type WsMessageOneOf13TypeEnum = typeof WsMessageOneOf13TypeEnum[keyof typeof WsMessageOneOf13TypeEnum];


/**
 * Check if a given object implements the WsMessageOneOf13 interface.
 */
export function instanceOfWsMessageOneOf13(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "workspace" in value;
    isInstance = isInstance && "host" in value;
    isInstance = isInstance && "type" in value;

    return isInstance;
}

export function WsMessageOneOf13FromJSON(json: any): WsMessageOneOf13 {
    return WsMessageOneOf13FromJSONTyped(json, false);
}

export function WsMessageOneOf13FromJSONTyped(json: any, ignoreDiscriminator: boolean): WsMessageOneOf13 {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'workspace': json['workspace'],
        'host': SimpleHostFromJSON(json['host']),
        'type': json['type'],
    };
}

export function WsMessageOneOf13ToJSON(value?: WsMessageOneOf13 | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'workspace': value.workspace,
        'host': SimpleHostToJSON(value.host),
        'type': value.type,
    };
}

